import axios from 'axios';
import type { AxiosInstance, AxiosError } from 'axios';
import { signupSchema, tokenSchema, type signupData, type Token } from '$lib/schemas/auth';
// validating email depending if it's a supervisor email or just an email for signing up
type ValidateEmail = 'supervisor' | 'email';
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
			// const { data } = await this.api.get('/');
			// return data.message;
			return 'hello wink';
		} catch (error) {
			throw new Error(`Failed to create photo: ${error}`);
		}
	}
	async signUserUp(form: signupData): Promise<Token> {
		try {
			// const { data } = await this.api.post('/signup', form);
			// return tokenSchema.parse(data);
			return tokenSchema.parse({ refresh_token: '', access_token: '', token_type: '' });
		} catch (error) {
			throw new Error(`Failed to signup: ${error}`);
		}
	}
	async validateEmail(email: string, type: ValidateEmail): Promise<string> {
		try {
			// const { data } = await this.api.get(`/auth/validate-${type}?email=${email}`);
			// return data.message;
			return 'valid';
		} catch (error) {
			throw new Error(`Failed to create photo: ${error}`);
		}
	}
}
