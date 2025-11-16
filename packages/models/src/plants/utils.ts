import { Lifespan } from "./schema.js";

type ObservationId = 'seed' | 'germ' | 'expiry' | 'dormancy' | 'growth'

type LifespanDateKeys = keyof Lifespan['dates'];
const lifespanDateKeyToObservationId: Record<LifespanDateKeys, ObservationId> = {
    'seedDate': 'seed',
    'germDate': 'germ',
    'expiryDate': 'expiry',
    'dormancyDates': 'dormancy',
    'growthDates': 'growth'
}

/**
 * Converts a lifespan object to a list of dates of observations.
 * @param lifespan The lifespan to convert.
 * @returns All recorded observations.
 */
export function lifespanDates(lifespan: Lifespan | null) {
    if (!lifespan) return []

    const result: {date: Date, observation: ObservationId}[] = []

    for(const key of Object.keys(lifespanDateKeyToObservationId) as LifespanDateKeys[]) {
        if(lifespan.dates[key] instanceof Set) {
            for (const value of lifespan.dates[key]) {
                if (value instanceof Date) {
                    result.push({date: value, observation: lifespanDateKeyToObservationId[key]})
                }
            }
        } else if (lifespan.dates[key] instanceof Date) {
            result.push({date: lifespan.dates[key], observation: lifespanDateKeyToObservationId[key]})
        }
    }
    return result
}