import os
import sys
sys.path.append('../')
import test_config
import importlib



def check_datatype(data_type):
    for dt in test_config.datatypes:
        if dt in data_type.lower():
            return test_config.datatypes[dt]
    return None



class Test:
	def __init__(self):
		self.dict = {}


	# 遍历测试套件：获取某一数据格式（project+datatype）的测试结果
	def traverse(self, input_path, project, datatype=None):
		# 注意，这个config.tasks应该重新定义
		if (project, datatype) in test_config.tasks:
			processor_class = importlib.import_module(test_config.tasks[(project, datatype)])
			processor = processor_class.Execute()
			if hasattr(processor, "run"):
				run = getattr(processor, "run")
				# 添加键值对
				self.dict[(project, datatype)] = run(input_path)
		else:
			if datatype is None:
				datatype = ""
			print("当前不支持以下数据格式操作：" + project + " " + datatype)


	def exportReport(self, output_path):
		return


	def run(self, input_dir):
		# suite_name 对应GPR等类型的文件夹
		for suite_name in os.listdir(input_dir):
			# 验证是否为目录结构
			if not os.path.isdir(os.path.join(input_dir, suite_name)):
				continue
			# 查看是否应对应处理方式
			if suite_name not in test_config.projects.keys():
				print("该测试套件" + suite_name + " 无对应方法调用。")
				continue

			need_dt = test_config.projects[suite_name]
			if need_dt:
				for data_type in os.listdir(os.path.join(input_dir, suite_name)):
					dt = check_datatype(data_type)
					input_path = os.path.join(input_dir, suite_name, data_type)
					self.traverse(input_path, suite_name, dt)
			else:
				input_path = os.path.join(input_dir, suite_name)
				self.traverse(input_path, suite_name)

		# 测试
		for key, value in self.dict.items():
			print(key)
			print(value)





if __name__ == "__main__":
	# 默认输入输出地址
	if len(sys.argv) == 1:
		suite_dir = "./suite"
		if not os.path.exists(suite_dir):
			raise FileNotFoundError("输入测试用例" + suite_dir + "不存在！")
		report_dir = "./output"
		if not os.path.exists(report_dir):
			os.makedirs(report_dir)
	# 自定义输入输出地址
	elif len(sys.argv) == 3:
		suite_dir = sys.argv[1]
		report_dir = sys.argv[2]
		if not os.path.exists(suite_dir):
			raise FileNotFoundError("输入测试用例" + suite_dir + "不存在！")
		if not os.path.exists(report_dir):
			os.makedirs(report_dir)
	else:
		raise ValueError("输入参数个数不正确！")

	test = Test()
	test.run(suite_dir)
	test.exportReport(report_dir)

