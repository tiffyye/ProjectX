
//Helper function to display Javascript value on HTML page
function showResponse(response) 
{
    var responseString = JSON.stringify(response, '', 2);
    document.getElementById('response').innerHTML += responseString;
}

//Called automatically when Javascript client library is loaded
function onClientLoad()
{
    gapi.client.load('youtube', 'v3', onYouTubeApiLoad);
}

//Called automatically when YouTube API interface is loaded.
function onYouTubeApiLoad()
{
    gapi.client.setApiKey('/*some ID need to register here https://developers.google.com/console/help/#generatingdevkeys*/');
}

function search()
{//Use the JS client library to create a search.list() API call.
    var request = gapi.client.youtube.search.list({
	part: 'id'.
	q: 'china'
    });
    //Send the request to the API server
    //and invoke onSearchResponse() with the response.
    request.execute(onSearchResponse);
}

//Called automatically with the response of the Youtube API request.
function onSearchResponse(response) 
{
    showResponse(response);
}
