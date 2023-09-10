def covid_stats():
	#Load current count
	counter_read_file=open("count.txt","r")
	visitors_count=int(counter_read_file.read())
	counter_read_file.close()

	text=requests.form['text']

	corona_data='https://covidstats-sdbd.onrender.com/?country='+text
	print(corona_data)
	return render_template("index.html",image=corona_data,count=visitors+count)