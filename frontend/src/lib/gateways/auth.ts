import axios from 'axios';
import type { AxiosInstance, AxiosError } from 'axios';
export interface Token {
	access_token: string;
	refresh_token: string;
	token_type: string;
}
export interface AuthGateway {
	connectToDB(): Promise<string>;
	signUserUp(): Promise<Token>;
	signUserIn(): Promise<Token>;
}
export class AuthGateaway implements AuthGateaway {
	private api: AxiosInstance;

	constructor() {
		this.api = axios.create({
			baseURL: import.meta.env.VITE_API_BASE_URL,
			timeout: 5000,
			headers: {
				'Content-Type': 'application/json'
			}
		});
		this.api.interceptors.response.use(
			(response) => response,
			(error: AxiosError) => {
				console.error('API:', error.message);
				return Promise.reject(error.response?.data || error.message);
			}
		);
	}
	async connectToDB(): Promise<string> {
		try {
			const { data } = await this.api.get('/');
			return data.message;
		} catch (error) {
			throw new Error(`Failed to create photo: ${error}`);
		}
	}
	async sign
}
