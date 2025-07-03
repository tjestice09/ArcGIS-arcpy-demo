import arcpy
arcpy.env.workspace = r"C:\Users\tjestice09\Documents\ArcGIS\Projects\CampgroundBufferTool\CampgroundBufferTool.gdb"
arcpy.env.overwriteOutput = True

input_fc = "Campgrounds"

output_fc = "Campgrounds_Buffer"

arcpy.Buffer_analysis(
    in_features=input_fc,
    out_feature_class=output_fc,
    buffer_distance_or_field="1 Miles",
    line_side="FULL",
    line_end_type="round",
    dissolve_option="NONE"
)
print("Buffer created successfully!")