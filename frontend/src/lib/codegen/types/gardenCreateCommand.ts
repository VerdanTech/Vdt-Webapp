/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */
import type { GardenCreateCommandKey } from './gardenCreateCommandKey'
import type { GardenCreateCommandVisibility } from './gardenCreateCommandVisibility'

export interface GardenCreateCommand {
	admin_usernames?: string[]
	/**
	 * Must be at most 1400 characters
	 * @maxLength 1400
	 */
	description?: string
	editor_usernames?: string[]
	key?: GardenCreateCommandKey
	/**
	 * Must be between 2 and 50 characters long and contain only alphanumeric characters and spaces
	 * @minLength 2
	 * @maxLength 50
	 * @pattern [0-9A-Za-z ]+
	 */
	name: string
	viewer_usernames?: string[]
	visibility?: GardenCreateCommandVisibility
}
