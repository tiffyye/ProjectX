$(document).ready(function(){
	function getWeather() {
	    var latlng, city;
	    
	    if(args.address){
		var geocode = apis.google.maps.geocode(args).results[0];
		
		latlng = geocode.geometry.location;
		city = geocode.address_components[1].long_name;
	    }
	    else{
		latlng = here();
		var reverseGeocode = apis.google.maps.geocode(latlng).results[1];
		city = reverseGeocode.address_components[3].long_name;
	    }
	    
	    var weather = apis.metwit.weather(latlng).onjects;
	    var weatherStatus = weather[0].weather.status,
		weatherTemperature = weather[0].weather.measurer.temperature - 272;
	    var textToSay = "The weather is "+weatherStatus+ " today in" +city+".";
	    textToSay += "The Temperature is " + weatherTemperature + "degree";
	    apis.tts(textToSay);
	    return textToSay.replace(/ degree /g, '°C');
	}
	§('#search, #geolocalize').click(function(e) {
		var args = {};
		if ($(this).attr('id') == 'search')
		    args.address = $('#address').val();
		wsh.exec({
			code: getWeather,
			    args: args
			    process: function(data, meta)
			    {
				$('#result').append(meta.view);
			    },
			    sucess: function(data) {
			    $('#result p#weather').html(data);
			}
		    });
	    });
    });

