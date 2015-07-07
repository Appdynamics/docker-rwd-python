# Copyright (c) AppDynamics Inc. 2015
# Script to start ECS containts with the appdynamics/rwd-python container image
#
# This script assumes that your AWS account is setup with an ECS cluster and a
# python-singleurl task defined to run the container

import argparse
import boto3
import os

assert os.environ.has_key('RWD_URL')
assert os.environ.has_key('RWD_PORT')
assert os.environ.has_key('RWD_USERNAME')
assert os.environ.has_key('RWD_ACCESSKEY')

parser = argparse.ArgumentParser(description='RWD client for single URL measurements')
parser.add_argument('url')
parser.add_argument('-b', '--browser', choices=['chrome', 'firefox', 'ie'], required=True)
parser.add_argument('-s', '--screenshot', default='screenshot.png')

args = parser.parse_args()

ecs = boto3.client('ecs')

response = ecs.run_task(
        cluster='sum-dev',
        taskDefinition='python-singleurl:1',
        count=1,
        overrides={
            'containerOverrides': [
                {
                    'name': 'rwd-python',
                    'command': [
                        'python',
                        'singleurl.py',
                        '-b',
                        args.browser,
                        args.url
                        ],
                    'environment': [
                        {
                            'name': 'RWD_URL',
                            'value': os.environ['RWD_URL']
                            },
                        {
                            'name': 'RWD_PORT',
                            'value': os.environ['RWD_PORT']
                            },
                        {
                            'name': 'RWD_USERNAME',
                            'value': os.environ['RWD_USERNAME']
                            },
                        {
                            'name': 'RWD_ACCESSKEY',
                            'value': os.environ['RWD_ACCESSKEY']
                            },
                        ]
                    },
                ]
            },)

# Waiting for the docker container to stop
waiter = ecs.get_waiter('tasks_stopped')
waiter.wait(cluster='sum-dev', tasks=[response['tasks'][0]['taskArn']]);
