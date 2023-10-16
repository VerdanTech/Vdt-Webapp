//Object to catch errors returned by API
export interface ErrorResponse {
	non_field_errors?: string[];
	[key: string]: string[] | undefined;
}
