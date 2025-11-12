import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import type { initialUser } from '$lib/schemas/auth';
import { jwtDecode } from 'jwt-decode';
import { isTokenValid } from '$lib/utils/auth';

let initialAccessToken = null;
let initialUser = null;
if (browser) {
	const storedToken = localStorage.getItem('accessToken');
	if (storedToken && isTokenValid(storedToken)) {
		initialAccessToken = storedToken;
		const payload = jwtDecode(storedToken);
		initialUser = { email: payload.sub };
	} else {
		console.log('error');
	}
}

export const user = writable({
	accessToken: initialAccessToken,
	user: initialUser,
	isAuthenticated: !!initialAccessToken
});

export const updateUser = (accessToken: string) => {
	const payload = jwtDecode(accessToken);
	initialUser = { email: payload.sub };
	localStorage.setItem('accessToken', accessToken);

	user.set({ accessToken, user: initialUser, isAuthenticated: !!accessToken });
};
