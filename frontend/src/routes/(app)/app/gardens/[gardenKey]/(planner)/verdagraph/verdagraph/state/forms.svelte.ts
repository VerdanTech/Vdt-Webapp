import type { Component } from 'svelte';
import AddForm from '../forms/AddForm.svelte';
import TranslateForm from '../forms/TranslateForm.svelte';
import DeleteForm from '../forms/DeleteForm.svelte';
import ObserveForm from '../forms/ObserveForm.svelte';
import PatternsForm from '../forms/PatternsForm.svelte';
import PlansForm from '../forms/PlansForm.svelte';
import GeneratorsForm from '../forms/GeneratorsForm.svelte';
import FilterForm from '../forms/FilterForm.svelte';

export type VerdagraphFormType =
	| 'add'
	| 'translate'
	| 'delete'
	| 'observe'
	| 'patterns'
	| 'plans'
	| 'generators'
	| 'filter';

type FormAttributeType = {
	id: VerdagraphFormType;
	label: string;
	content: Component;
};

const formAttributes: FormAttributeType[] = [
	{ id: 'add', label: 'Add', content: AddForm },
	{ id: 'translate', label: 'Translate', content: TranslateForm },
	{ id: 'delete', label: 'Delete', content: DeleteForm },
	{ id: 'observe', label: 'Observe', content: ObserveForm },
	{ id: 'patterns', label: 'Patterns', content: PatternsForm },
	{ id: 'plans', label: 'Plans', content: PlansForm },
	{ id: 'generators', label: 'Generators', content: GeneratorsForm },
	{ id: 'filter', label: 'Filter', content: FilterForm }
];

/** Runes */

/** Stores the IDs of the active forms. */
let activeFormIds = $state<VerdagraphFormType[]>([]);
/** Stores the ID of the last activated form. */
let lastActivatedId = $state<VerdagraphFormType | undefined>();
/** Presents the attributes of the active forms. */
let activeForms = $derived(
	formAttributes.filter((attributes) => activeFormIds.includes(attributes.id))
);
/** Presents true if any forms are active. */
let anyFormsActive = $derived(activeFormIds.length > 0);

/**
 * Form management for the Verdagraph.
 */
export const forms = {
	/** Getters. */
	get lastActivatedId(): VerdagraphFormType | undefined {
		return lastActivatedId;
	},
	get activeForms(): FormAttributeType[] {
		return activeForms;
	},
	get anyFormsActive(): boolean {
		return anyFormsActive;
	},

	/** Setters. */
	set lastActivatedId(newVal: VerdagraphFormType) {
		lastActivatedId = newVal;
	},

	/**
	 * Activates a form.
	 * @param id ID of the form to activate.
	 * @param options Used to configure initial data for forms.
	 */
	activateForm(id: VerdagraphFormType, options?: Record<string, any>) {
		if (!activeFormIds.includes(id)) {
			activeFormIds.push(id);
		}
		lastActivatedId = id;
	},
	/**
	 * Deactivate a form.
	 * @param id ID of the form to deactivate
	 */
	deactivateForm(id: VerdagraphFormType) {
		if (activeFormIds.includes(id)) {
			activeFormIds = activeFormIds.filter((item) => item !== id);
		}
		if (!anyFormsActive) {
			lastActivatedId = undefined;
		}
	}
};
export default forms;
