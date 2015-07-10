# Copyright (c) AppDynamics Inc. 2015
# Script to start ECS containts with the appdynamics/rwd-python container image
#
# This script assumes that your AWS account is setup with an ECS cluster and a
# python-singleurl task defined to run the container

import argparse
import sys
import boto3
import os

parser = argparse.ArgumentParser(description='RWD client for single URL measurements')

ie_browsers = [ 'ie 10', 'ie 11' ]
browsers =  ['chrome', 'firefox', 'internet explorer'] + ie_browsers

parser.add_argument('--server-url', required=True)
parser.add_argument('--test-url', required=True)
parser.add_argument('--browser', choices=browsers, required=True)
parser.add_argument('--screenshot', default='screenshot.png')
parser.add_argument('--firefox-profile-dir')
parser.add_argument('browser_args', nargs='*')

args = parser.parse_args()

command = ['python', 'singleurl.py'] + sys.argv[1:]

ecs = boto3.client('ecs')

response = ecs.run_task(
        cluster='sum-dev',
        taskDefinition='python-singleurl:2',
        count=1,
        overrides={
            'containerOverrides': [
                {
                    'name': 'rwd-python',
                    'command': command,
                },
            ]
        },)

# Waiting for the docker container to stop
waiter = ecs.get_waiter('tasks_stopped')
waiter.wait(cluster='sum-dev', tasks=[response['tasks'][0]['taskArn']]);
