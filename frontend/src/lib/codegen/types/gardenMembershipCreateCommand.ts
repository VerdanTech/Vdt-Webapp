/**
 * Generated by orval v6.31.0 🍺
 * Do not edit manually.
 * VerdanTech-Backend
 * Backend API of the VerdanTech software project.
 * OpenAPI spec version: 0.1.0
 */

export interface GardenMembershipCreateCommand {
	admin_usernames?: string[]
	editor_usernames?: string[]
	garden_id: string
	viewer_usernames?: string[]
}
