import { z } from 'zod';
import { AuthGateaway } from '$lib/gateways/auth';
const gateway = new AuthGateaway();

export const roleSchema = z.object({
	role: z
		.enum(['supervisor', 'employee'], {
			message: 'Выберите роль',
			required_error: 'Выберите роль'
		})
		.default('')
});
export const tokenSchema = z.object({
	access_token: z.string(),
	refresh_token: z.string(),
	token_type: z.string()
});

export const baseSignupSchema = z
	.object({
		fullname: z.string(),
		email: z.string().email({ message: 'Некоректный email' }),
		password: z.string().min(8, { message: 'Пароль слишком короткий, от 8 символов' }),
		confirm: z.string()
	})
	.refine((data) => data.password === data.confirm, {
		message: 'Пароли не совпадают',
		path: ['confirm']
	})
	.refine(
		(data) => data.fullname.split(' ').length === 3 && data.fullname.split(' ').indexOf('') === -1,
		{
			message: 'ФИО неккоректно',
			path: ['fullname']
		}
	)
	.refine((data) => gateway.validateEmail(data.email, 'email'), {
		message: 'Почта уже занята',
		path: ['email']
	});
export const supervisorSchema = baseSignupSchema.safeExtend({
	role: z.enum(['supervisor', 'employee']).default('supervisor')
});
export const employeeSchema = baseSignupSchema
	.safeExtend({
		role: z.enum(['supervisor', 'employee']).default('employee'),
		supervisor_email: z.string().email({ message: 'Некоректный email' })
	})
	.refine((data) => gateway.validateEmail(data.supervisor_email, 'supervisor'), {
		message: 'Руководителя с такой почтой не существует',
		path: ['supervisor_email']
	});

export const loginSchema = z.object({
	email: z.string().email({ message: 'Некоректный email' }),
	password: z.string().nonempty({ message: 'Пароль не может быть пустым' })
});
export const signupSchema = z.object({
	firstname: z.string(),
	surname: z.string(),
	lastname: z.string(),
	email: z.string().email({ message: 'Некоректный email' }),
	password: z.string().min(8, { message: 'Пароль слишком короткий, от 8 символов' }),
	role: z.enum(['supervisor', 'employee']),
	supervisor_email: z.string().default('')
});

export type signupData = z.infer<typeof signupSchema>;
export type loginData = z.infer<typeof loginSchema>;
export type Token = z.infer<typeof tokenSchema>;
