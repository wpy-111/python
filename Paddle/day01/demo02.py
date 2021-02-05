import numpy as np
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph #动态图加载
from paddle.fluid.dygraph import Linear
import sklearn.datasets as sd
class Regressor(fluid.dygraph.Layer):
    def __init__(self):
        super(Regressor, self).__init__()
        self.fc = Linear(input_dim=13,output_dim=1,act=None)
    #网络的前向计算
    def forward(self, inputs):
        x = self.fc(inputs)
        return x
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
        data[:,i] = (data[:,i] - avg_values[i]) / (max_values[i] - min_values[i])
    print(data.shape)
    return data
def process():
    data = sd.load_boston()
    size = int(len(data.data) * 0.8)
    x = data.data[size:, :]
    y = data.target[size:]
    data = np.column_stack((x, y))
    for i in range(data.shape[1]):
        data[:, i] = (data[:, i] - avg_values[i]) / (max_values[i] - min_values[i])
    return data
with dygraph.guard():
    one = load_data()
    data = process()
    data = np.array(data).astype('float32')
    test_x = data[:,:-1]
    test_y = data[:,-1]
    x = fluid.dygraph.to_variable(test_x)
    model = Regressor()
    # 参数为保存模型参数的文件地址
    model_dict,_ = fluid.load_dygraph('LR_model')
    model.load_dict(model_dict)
    model.eval()
    # 参数为数据集的文件地址
    # test_data,label = load_one_example()
    # 将数据转为动态图的variable格式
    results = model(x)
    # 对结果做反归一化处理
    y = test_y * (max_values[-1] - min_values[-1]) + avg_values[-1]
    results = results * (max_values[-1] - min_values[-1]) + avg_values[-1]
    for result,real in zip(results,y):
        print("Inference result is {}, the corresponding label is {}".format(result.numpy(), real))
