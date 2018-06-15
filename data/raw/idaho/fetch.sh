curl -L \
  'https://services1.arcgis.com/CNPdEkvnGl65jCX8/arcgis/rest/services/VsnWn/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=1000' \
  | jq '.' \
  > idaho-vax-exemptions-arcgis.json
