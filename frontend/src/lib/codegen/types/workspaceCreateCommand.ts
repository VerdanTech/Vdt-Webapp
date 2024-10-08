/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { WorkspaceCreateCommandDescription } from './workspaceCreateCommandDescription';

export interface WorkspaceCreateCommand {
	description?: WorkspaceCreateCommandDescription;
	/**
	 * Must be between 4 and 16 characters long and contain only alphanumeric characters and hyphens
	 * @minLength 4
	 * @maxLength 16
	 * @pattern [0-9A-Za-z-]+
	 */
	garden_key: string;
	/**
	 * A descriptive name for this workspace. Must be between 3 and 30 characters long and contain only alphanumeric characters, spaces, hyphens, and underscores.
	 * @minLength 3
	 * @maxLength 30
	 * @pattern [0-9A-Za-z _-]+
	 */
	name: string;
}