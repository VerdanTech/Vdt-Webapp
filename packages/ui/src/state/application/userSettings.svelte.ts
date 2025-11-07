import { LocalStore } from '@vdg-webapp/ui';

export type UnitSystem = 'metric' | 'imperial';
export type UnitAwareQuantity = 'distance' | 'temperature' | 'mass' | 'volume';

type PreferredUnitSettings = {
	distance: UnitSystem;
	temperature: UnitSystem;
	mass: UnitSystem;
	volume: UnitSystem;
};

/**
 * Holds persisted user settings.
 */
export function createSettingsContext() {
	/** Unit settings. */
	const units = new LocalStore<PreferredUnitSettings>('unitSettings', {
		distance: 'metric',
		temperature: 'metric',
		mass: 'metric',
		volume: 'metric'
	});

	return {
		get units() {
			return units.value;
		},
		set units(newVal) {
			units.value = newVal;
		}
	};
}
export type SettingsContext = ReturnType<typeof createSettingsContext>;
