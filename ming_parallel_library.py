#!/usr/bin/python

from joblib import Parallel, delayed
import multiprocessing
import os

def run_shell_command(script_to_run):
	os.system(script_to_run)
	return "DONE"

#Wraps running in parallel a set of shell scripts
def run_parallel_shellcommands(input_shell_commands, parallelism_level):
	return run_parallel_job(run_shell_command, input_shell_commands, parallelism_level)

#Wraps the parallel job running, simplifying code
def run_parallel_job(input_function, input_parameters_list, parallelism_level):
	if parallelism_level == 1:
		output_results_list = []
		for input_param in input_parameters_list:
			result_object = input_function(input_param)
			output_results_list.append(result_object)
		return output_results_list
	else:
		results = Parallel(n_jobs = parallelism_level)(delayed(input_function)(input_object) for input_object in input_parameters_list)
		return results