import { PUBLIC_API_URL } from '$env/static/public'
//stuff that should be with each request here!
//e.g. no refresh check

//SPENT 4 FUCKING HOURS TRYING TO INTERCEPT FETCH REQUEST
//NEVER TOUCH THIS GARBAGE AGAIN
//THIS DUMB PILE OF SHIT REWRITES POST REQUEST AS GET
//HAS TROUBLE ENCODING REQUESTS AND PASSES FUCKING EMPTY REQUEST BODIES
//I'VE LOST 4 (!!!) HOURS OF MY LIFE WITH NEGATIVE EFFICIENCY
//MY EYES ARE RED AND MY HEAD HURTS
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT
//FUCK THIS STUPID SHIT

/*
export async function handleFetch({ event, request, fetch }) {
	const headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Bearer ' + event.cookies.get('access')
    }
	
	const url = new URL(request.url) 
	console.log(request.method) //method: POST
	if (url.pathname.startsWith('/')) {
		request = new Request(
			PUBLIC_API_URL + url.pathname,
			{
				...request,
				headers: headers,
			}
		)
	}
	console.log(request) //method: GET AHAHAHAHAHAHHAHAHA, HOW THE FUCK DID IT HAPPEN?
	return fetch(request)
}
*/