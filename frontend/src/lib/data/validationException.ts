/** The type of data returned on 400 Validation Exceptions */
export interface ValidationException {
	detail: string;
	extra: Array<{ key: string; message: string }>;
}
