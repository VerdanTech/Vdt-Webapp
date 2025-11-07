import { ZodType } from 'zod';

/**
 * Validates a single field against a schema.
 * @param value The value to validate.
 * @param schema The schema to validate it against.
 * @returns A list of errors, or undefined if validation was successful.
 */
export declare function validateField(
	value: any,
	schema: ZodType
): string[] | undefined;
//# sourceMappingURL=utils.d.ts.map
