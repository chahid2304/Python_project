import folium
import pandas

data=pandas.read_excel("iit_data.xlsx")
rank=list(data["IIT Ranking"])
college_name=list(data["IIT College"])
Nirf_score=list(data["NIRF Score"])
lat=list(data["Latitude"])
lon=list(data["Longitude"])
pic=list(data["Image"])

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

#fg.add_child(folium.Marker(location=[27.1751, 78.0421],popup="this is were taj mahal is located  "))
for ranki,name,score,lati,longi,image in zip(rank,college_name,Nirf_score,lat,lon,pic):
    fg.add_child(folium.Marker(location=[lati,longi],popup="<b>College name:</b>"+str(name)
    +"<br><b>Rank amoong IIT in India :</b>"+str(ranki)
    +"<br><b>Nirf score:</b>"+str(score)
    +"<br><b>image:</b>"+image+"height=145,width=300",icon=folium.Icon(color="red")))

map=folium.Map(location=[21.1458,79.0882],zoom_start=5)

map.add_child(fg)
map.save("test.html")