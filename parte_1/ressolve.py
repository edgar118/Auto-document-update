import os
import json

###################################################################################
# This function helps you to test your solution using validation_test.json
###################################################################################
def validate_function(function_name):
	validation_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validation_test.json")
	validation_test = {}
	with open(validation_file_path, 'r') as f:
		validation_test = json.load(f)
	
	test_list = None
	try:
		test_list = validation_test[function_name]
	except:
		print("Error - the function name does not exits in the validation test json")
		exit(1)
	print("Total test found: {}".format(len(test_list)))
	test_ok = 0
	for index, test in enumerate(test_list):
		input_value = test['input']
		result = globals()[function_name](input_value)
		if result == test['output']:
			print("Test {} -> input: {} expected: {} function result: {} -> OK".format(index, test['input'], test['output'], result))
			test_ok += 1
		else:
			print("Test {} -> input: {} expected: {} function result: {} -> FAILED".format(index, test['input'], test['output'], result))

	print("Total tests passed: {} Total tests failed: {}".format(test_ok, int(len(test_list) - test_ok)))

def list_average(input_value):
	output, num, sum = 0, 0, 0
	flag = 1

	for i in input_value:
		if i != 10:
			if flag == 1:
				sum += i
				num += 1
		else:
			flag = flag * -1
	if num == 0:
		num = 1
	output = sum//num

	return output

def multiplies_numbers(input_value : str):
	output = 1
	n = ""

	for i in input_value + " ":
		if i.isnumeric():
			n += i
		else:
			if n != "":
				output *= int(n)
			n = ""

	return output

def christmas_tree(input_value):
	up = input_value//2

	for i in range(1, input_value + 2):
		line = [" " for _ in range(input_value)]
		line[up] = "*" # horizontal half

		if i <= up + 1:	
			for j in range(1, i):
				line[up - j] = "*"
				line[up + j] = "*"

		print("".join(line))	



validate_function('list_average') # Put your function here
validate_function('multiplies_numbers') # Put your function here

christmas_tree(15)
christmas_tree(7)
christmas_tree(3)