import {z} from "jazz-tools"

import { commonFields } from '../commands.js';

/**
 * Specifies a type of geometry.
 * Each geometry type is associated with a different record type
 * describing its features.
 * RECTANGLE: a closed shape specified by width and height.
 * POLYGON: a closed shape specified by a number of sides and their length.
 * ELLIPSE: a closed shape specified by a major and minor radius.
 * LINES: a closed or open shape specified by a set of joined line segments.`
 */
export const GeometryTypeEnumOptions = [
	'RECTANGLE',
	'POLYGON',
	'ELLIPSE',
	'LINES'
] as const;

/** Field specifications for workspace domain commands. */
const workspaceFields = {
	workspaceNameField: commonFields.nameSchema.describe(
		'Name of the workspace. Must be unique within a garden.'
	),
	workspaceDescriptionField: commonFields.descriptionSchema.describe(
		'Optional description.'
	),
	plantingAreaNameField: commonFields.nameSchema.describe(
		'The name of the planting area.'
	),
	plantingAreaDescriptionField: commonFields.descriptionSchema.describe(
		'Optional description.'
	),
	plantingAreaDepthField: z
		.number()
		.min(0, 'May not be negative')
		.max(1000, 'May be at most 1000m.')
		.describe('The depth of the planting area.'),
	coordinateXField: z
		.number()
		.min(-1000000, 'Limited to 1 000 000 meters.')
		.max(1000000, 'Limited to 1 000 000 meters.')
		.describe('The horizontal X component of the coordinate.'),
	coordinateYField: z
		.number()
		.min(-1000000, 'Limited to 1 000 000 meters.')
		.max(1000000, 'Limited to 1 000 000 meters.')
		.describe('The vertical Y component of the coordinate.'),
	coordinateField: z
		.object({
			x: z
				.number()
				.min(-1000000, 'Limited to 1 000 000 meters.')
				.max(1000000, 'Limited to 1 000 000 meters.')
				.describe('The horizontal X component of the coordinate.'),
			y: z
				.number()
				.min(-1000000, 'Limited to 1 000 000 meters.')
				.max(1000000, 'Limited to 1 000 000 meters.')
				.describe('The vertical Y component of the coordinate.')
		})
		.describe('A position relative to the origin of a workspace or a geometry.'),
	locationDateField: z.date().describe('The date at which the location applies.'),
	geometryTypeField: z
		.literal(GeometryTypeEnumOptions)
		.describe(
			'Describes the type of geometry. Each type has a unique set of attributes associated with it.'
		),
	geometryDateField: z
		.date()
		.describe('The date at which the geometry applies to the object.'),
	geometryScaleFactorField: z
		.number()
		.min(0.01, 'Must be at least 1%.')
		.max(100, 'May be at most 10000%')
		.describe(
			'Factor used to scale the geometry up or down. Must be within 1 and 1000 percent.'
		),
	geometryRotationField: z
		.number()
		.min(-360, 'Must be at least negative 360 degrees.')
		.max(360, 'May be at most 360 degrees.')
		.describe(
			'The rotation of the geometry in degrees. Must be between 0 and 360 degrees.'
		),
	geometryRectangleLengthField: z
		.number()
		.min(0.01, 'May not be negative or zero.')
		.max(1000, 'May be at most 1000m')
		.describe('The horizontal, or x-axis length of the rectangle.'),
	geometryRectangleWidthField: z
		.number()
		.min(0.01, 'May not be negative or zero.')
		.max(1000, 'May be at most 1000m')
		.describe('The vertical, or y-axis width of the rectangle.'),
	geometryPolygonNumSidesField: z
		.number()
		.min(3, 'Must have at least 3 sides.')
		.max(20, 'May have at most 20 sides.')
		.describe('The amount of sides the polygon has.'),
	geometryPolygonRadiusField: z
		.number()
		.min(0.01, 'May not be negative or zero.')
		.max(1000, 'May be at most 1000m')
		.describe('The distance from the center to any vertex of the polygon.'),
	geometryEllipseLengthField: z
		.number()
		.min(0.01, 'May not be negative or zero.')
		.max(1000, 'May be at most 1000m.')
		.describe('The horizontal, or x-axis diameter of the ellipse.'),
	geometryEllipseWidthField: z
		.number()
		.min(0.01, 'May not be negative or zero.')
		.max(1000, 'May be at most 1000m')
		.describe(
			'The vertical, or y-axis diameter of the ellipse. Must be between 0 and 1000 meters.'
		),
	geometryLinesCoordinatesField: z
		.array(
			z
				.object({
					x: z
						.number()
						.min(-1000000, 'Limited to 1 000 000 meters.')
						.max(1000000, 'Limited to 1 000 000 meters.')
						.describe('The horizontal X component of the coordinate.'),
					y: z
						.number()
						.min(-1000000, 'Limited to 1 000 000 meters.')
						.max(1000000, 'Limited to 1 000 000 meters.')
						.describe('The vertical Y component of the coordinate.')
				})
				.describe('A position relative to the origin of a workspace or a geometry.')
		)
		.min(3, 'Must have at least 3 points.')
		.describe(
			'A list of coordinates relative to the position of the geometry which define an irregular polygonal.'
		),
	geometryLinesClosedField: z
		.boolean()
		.describe('If true, the line segments form a closed shape.')
};
export default workspaceFields;
