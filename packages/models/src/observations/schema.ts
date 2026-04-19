import {co, z} from "jazz-tools"

export const ObservationSchema = co.map({
	date: z.date(),
	title: z.string(),
	notes: co.plainText()
})

export type GenericObservation = co.loaded<typeof ObservationSchema>;
