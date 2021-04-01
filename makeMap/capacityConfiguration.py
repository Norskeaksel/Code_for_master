c={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "Power Capacities"
          ],
          "id": "4ol9ypje",
          "name": [
            "Timestamp"
          ],
          "type": "timeRange",
          "value": [
            1420070400000,
            1420070400001
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "incremental",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "xfa6mc7",
          "type": "geojson",
          "config": {
            "dataId": "Power Capacities",
            "label": "Power Capacities",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
              ],
              "colorRange": {
                "name": "ColorBrewer RdYlGn-9",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#d73027",
                  "#f46d43",
                  "#fdae61",
                  "#fee08b",
                  "#ffffbf",
                  "#d9ef8b",
                  "#a6d96a",
                  "#66bd63",
                  "#1a9850"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "Share Renewable",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Power Capacities": [
              {
                "name": "Region",
                "format": None
              },
              {
                "name": "Country",
                "format": None
              },
              {
                "name": "Scenario",
                "format": None
              },
              {
                "name": "Year",
                "format": None
              },
              {
                "name": "Value Type",
                "format": None
              },
              {
                "name": "Hydro",
                "format": None
              },
              {
                "name": "PV",
                "format": None
              },
              {
                "name": "Thermal",
                "format": None
              },
              {
                "name": "Wind Offshore",
                "format": None
              },
              {
                "name": "Wind Onshore",
                "format": None
              },
              {
                "name": "Percent Renawable",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 45.78659425960939,
      "longitude": 17.188245290164147,
      "pitch": 0,
      "zoom": 2.3913897969209255,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}