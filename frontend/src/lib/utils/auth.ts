import { jwtDecode } from 'jwt-decode';
import type { initialUser } from '$lib/schemas/auth';
export function isTokenValid(token: string) {
	if (!token) return false;
	try {
		const payload: initialUser = jwtDecode(token);
		return payload?.exp > Date.now() / 1000;
	} catch {
		return false;
	}
}
