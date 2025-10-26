import { z } from 'zod';
export const roleSchema = z.object({
	role: z
		.enum(['supervisor', 'employee'], {
			message: 'Выберите роль',
			required_error: 'Выберите роль'
		})
		.default('')
});
export const signupSchema = z
	.object({
		fullname: z.string().min(1, { message: 'Фио обязательно' }),
		email: z.string().email({ message: 'Некоректный email' }),
		password: z.string().min(8, { message: 'Пароль слишком короткий, от 8 символов' }),
		confirm: z.string()
	})
	.refine((data) => data.password === data.confirm, {
		message: 'Пароли не совпадают',
		path: ['confirm']
	});

export const supervisorSchema = signupSchema.safeExtend({
	role: z.string().default('supervisor')
});
export const employeeSchema = signupSchema.safeExtend({
	role: z.string().default('employee'),
	supervisorEmail: z.string().email({ message: 'Некоректный email' })
});
