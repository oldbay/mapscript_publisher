# -*- coding: utf-8 -*-
# encoding: utf-8

import os, sys
from map_pub import BuildMapRes, PubMapWEB

if __name__ == "__main__":
    """
    script_name db_host
    """
    mapjsonfile = "./maps/rasters2pgsql.json"
    db_host = sys.argv[1]
    debug_path = "{}/GIS/mapserver/debug".format(os.environ["HOME"])
    
    # build map
    builder = BuildMapRes()
    builder.load4file(mapjsonfile)
    #builder.debug = True
    builder.debug = '{}/build.log'.format(debug_path)
    builder.mapjson["VARS"]["db_host"] = db_host 
    builder.build()
    
    # run web
    pubmap = PubMapWEB(builder.mapdict, port=3008)
    pubmap.debug_json_file(debug_path)
    pubmap.debug_python_mapscript(debug_path)
    pubmap.debug_map_file(debug_path)
    pubmap.wsgi()
