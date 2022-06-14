#!/bin/bash
cd /home/user/sources/download-sales-data && \
LUIGI_CONFIG_PATH=luigi_dev.cfg \
/home/user/envs/demo/bin/python -m luigi --module main \
DownloadSalesData >>luigi_dev.log 2>&1