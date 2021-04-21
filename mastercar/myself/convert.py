# 引用Paddlelite预测库
import paddlelite.lite as lite

# 1. 创建opt实例
opt=lite.Opt()
# 2. 指定输入模型地址
opt.set_model_file("F:\\python代码\\mastercar\\myself\\__model__\\__model__")
opt.set_param_file("F:\\python代码\\mastercar\\myself\\__model__\\__params__")
# 3. 指定转化类型： arm、x86、opencl、npu
opt.set_valid_places("x86")
opt.set_model_type('naive_buffer')
# 4. 输出模型地址
opt.set_optimize_out("mobilenetv1_opt")
# 5. 执行模型优化
opt.run()


