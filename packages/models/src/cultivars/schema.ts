import {co, z} from "jazz-tools"

import { CultivarAttributesSchema } from './attributes/index.js';
import { commonFields } from "../commands.js";


import fields from './fields.js'

export const CultivarSchema = co.map({
	name: fields.cultivarNameField,
	description: co.plainText(),
	abbreviation: fields.cultivarAbbreviationField,
	get parent() {
		return CultivarSchema
	},
	attributes: CultivarAttributesSchema,
	extra: co.map({
		fields.cultivarScientificNameField
	})
})


export const CultivarCollectionSchema = co.map({
	name: commonFields.nameSchema,
	description:  co.plainText(),
	priority: z.int(),
	get parent() {
		return CultivarCollectionSchema
	},
	cultivars: co.list(CultivarSchema)
})

export type CultivarAttributesSchema = z.infer<typeof CultivarCollectionSchema>
export type Cultivar = co.loaded<typeof CultivarSchema>;
export type CultivarCollection = co.loaded<typeof CultivarCollectionSchema>;
