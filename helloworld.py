import folium

#parent mappip
fg=folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(data=open("india_states.json","r",encoding="utf-8-sig").read()))
#utf means unicode transformation format
#8 for 8 bit 
#sig for signature
#html code to use our data set 

#for ranki,name,score,lati,longi,image in zip(rank,college_name,Nirf_score,lat,lon,pic):
   # fg.add_child(folium.Marker(location=[lati,longi],popup="<b>College name:</b>"+str(name)
    #+"<br><b>Rank amoong IIT in India :</b>"+str(ranki)
    #+"<br><b>Nirf score:</b>"+str(score)
    #+"<br><b>image:</b>"+image+"height=145,width=300",icon=folium.Icon(color="red")))

map=folium.Map(location=(200000,750000),zoom_start=4)
#latitude and longitude when you open your file 
map.add_child(fg)
map.save("final.html")