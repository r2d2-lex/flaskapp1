#!/bin/bash
#celery -A tasks worker --loglevel=info
celery -A tasks worker -B --loglevel=info
