"""
    波士顿房价预测
"""
import numpy as np
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph #动态图加载
from paddle.fluid.dygraph import Linear
import sklearn.datasets as sd
def load_data():
    data = sd.load_boston()
    size = int(len(data.data)*0.8)
    x = data.data[:size,:]
    y = data.target[:size]
    data = np.column_stack((x, y))
    maximum = data.max(axis=0)
    minimum = data.min(axis=0)
    avgs = data.sum(axis=0)/data.shape[0]
    global max_values
    global min_values
    global avg_values
    max_values = maximum
    min_values = minimum
    avg_values = avgs
    for i in range(data.shape[1]):
        data[:,i] = (data[:,i] - avgs[i]) / (maximum[i] - minimum[i])
    print(data.shape)
    return data
class Regressor(fluid.dygraph.Layer):
    def __init__(self):
        super(Regressor, self).__init__()
        self.fc = Linear(input_dim=13,output_dim=1,act=None)
    #网络的前向计算
    def forward(self, inputs):
        x = self.fc(inputs)
        return x
# 定义飞桨动态图的工作环境
with fluid.dygraph.guard():
    model = Regressor()
    # 开启模型训练模式
    model.train()
    #加载数据
    train_data = load_data()
    # 定义优化算法，这里使用随机梯度下降-SGD
    # 学习率设置为0.01
    opt = fluid.optimizer.SGD(learning_rate=0.01,parameter_list=model.parameters())
with dygraph.guard(fluid.CUDAPlace(0)):
    epoches = 10
    batches = 10
    for epoch in range(epoches):
        # 在每轮迭代开始之前，将训练数据的顺序随机的打乱
        np.random.shuffle(train_data)
        # 将训练数据进行拆分，每个batch包含10条数据
        mini_batches = [train_data[k:k+batches] for k in range(0,len(train_data),batches)]
        # 定义内层循环
        for iter_id,min_batch in enumerate(mini_batches):
            train_x = np.array(min_batch[:,:-1]).astype('float32') # 获得当前批次训练数据
            train_y = np.array(min_batch[:,-1]).astype('float32')  # 获得当前批次训练标签（真实房价）
            house_features = dygraph.to_variable(train_x)
            prices = dygraph.to_variable(train_y)
            # 前向计算
            predicts = model(house_features)
            # 计算损失
            loss = fluid.layers.square_error_cost(predicts,label=prices)
            avg_loss = fluid.layers.mean(loss)
            if iter_id % 20 == 0:
                print("epoch: {}, iter: {}, loss is: {}".format(epoch, iter_id, avg_loss.numpy()))
            # 反向传播
            avg_loss.backward()
            # 最小化loss,更新参数
            opt.minimize(avg_loss)
            # 清除梯度
            model.clear_gradients()
# 定义飞桨动态图工作环境
with dygraph.guard():
    # 保存模型参数，文件名为LR_model
    fluid.save_dygraph(model.state_dict(),'LR_model')
    print("模型保存成功，模型参数保存在LR_model中")
def load_one_example():
    datas = sd.load_boston()
    # 选择倒数第10条数据用于测试
    tmp = datas.data[-10]
    # 对数据进行归一化处理
    for i in range(13):
        tmp[i] = (tmp[i] - avg_values[i]) / (max_values[i] - min_values[i])
    data = np.array(tmp.astype(np.float32))
    label = datas.target[-10]
    return data, label

with dygraph.guard():
    # 参数为保存模型参数的文件地址
    model_dict, _ = fluid.load_dygraph('LR_model')
    model.load_dict(model_dict)
    model.eval()

    # 参数为数据集的文件地址
    test_data, label = load_one_example()
    # 将数据转为动态图的variable格式
    test_data = dygraph.to_variable(test_data)
    results = model(test_data)

    # 对结果做反归一化处理
    results = results * (max_values[-1] - min_values[-1]) + avg_values[-1]
    print("Inference result is {}, the corresponding label is {}".format(results.numpy(), label))

