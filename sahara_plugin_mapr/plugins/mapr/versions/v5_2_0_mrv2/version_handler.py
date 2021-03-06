# Copyright (c) 2015, MapR Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import sahara_plugin_mapr.plugins.mapr.base.base_version_handler as bvh
from sahara_plugin_mapr.plugins.mapr.services.drill import drill
from sahara_plugin_mapr.plugins.mapr.services.flume import flume
from sahara_plugin_mapr.plugins.mapr.services.hbase import hbase
from sahara_plugin_mapr.plugins.mapr.services.hive import hive
from sahara_plugin_mapr.plugins.mapr.services.httpfs import httpfs
from sahara_plugin_mapr.plugins.mapr.services.hue import hue
from sahara_plugin_mapr.plugins.mapr.services.impala import impala
from sahara_plugin_mapr.plugins.mapr.services.kafka import kafka
from sahara_plugin_mapr.plugins.mapr.services.mahout import mahout
from sahara_plugin_mapr.plugins.mapr.services.management import management
from sahara_plugin_mapr.plugins.mapr.services.maprfs import maprfs
from sahara_plugin_mapr.plugins.mapr.services.oozie import oozie
from sahara_plugin_mapr.plugins.mapr.services.pig import pig
from sahara_plugin_mapr.plugins.mapr.services.sentry import sentry
from sahara_plugin_mapr.plugins.mapr.services.spark import spark
from sahara_plugin_mapr.plugins.mapr.services.sqoop import sqoop2
from sahara_plugin_mapr.plugins.mapr.services.swift import swift
from sahara_plugin_mapr.plugins.mapr.services.yarn import yarn
import sahara_plugin_mapr.plugins.mapr.versions.v5_2_0_mrv2.context as c

version = "5.2.0.mrv2"


class VersionHandler(bvh.BaseVersionHandler):
    def __init__(self):
        super(VersionHandler, self).__init__()
        self._version = version
        self._required_services = [
            yarn.YARNv270(),
            maprfs.MapRFS(),
            management.Management(),
            oozie.Oozie(),
        ]
        self._services = [
            hive.HiveV12(),
            pig.PigV016(),
            impala.ImpalaV250(),
            flume.FlumeV16(),
            sqoop2.Sqoop2(),
            mahout.MahoutV012(),
            oozie.OozieV420(),
            hue.HueV310(),
            hue.HueLivyV310(),
            hbase.HBaseV111(),
            drill.DrillV19(),
            yarn.YARNv270(),
            maprfs.MapRFS(),
            management.Management(),
            httpfs.HttpFS(),
            swift.Swift(),
            sentry.SentryV16(),
            spark.SparkOnYarnV201(),
            kafka.Kafka(),
            kafka.KafkaConnect(),
            kafka.KafkaRest(),
        ]

    def get_context(self, cluster, added=None, removed=None):
        return c.Context(cluster, self, added, removed)
