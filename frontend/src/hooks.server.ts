import type { HandleFetch } from '@sveltejs/kit';
import { API_URL } from '$env/static/private';


//stuff that should be with each request here!
//e.g. no refresh check

/* 
export function handleFetch({ event, request, fetch }) {
	request.headers.set('Authorization', `Bearer ${event.cookies.get('access')}`)

	const url = new URL(request.url)
	if (url.pathname.startsWith('/')) {
		return fetch(API_URL + url.pathname, request)
	}

	console.log(request.headers)

	return fetch(request)
}
*/