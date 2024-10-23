import type { Component } from 'svelte';
import AddPlantingAreaForm from './forms/AddPlantingAreaForm.svelte';
import TranslateForm from './forms/TranslateForm.svelte';

export type WorkspaceEditorFormType = 'addPlantingArea' | 'translate';

type FormAttributeType = {
	id: WorkspaceEditorFormType;
	label: string;
	content: Component;
};

const formAttributes: FormAttributeType[] = [
	{ id: 'addPlantingArea', label: 'Add Planting Area', content: AddPlantingAreaForm },
	{ id: 'translate', label: 'Translate', content: TranslateForm }
];

/** Runes */

/** Stores the IDs of the active forms. */
let activeFormIds = $state<WorkspaceEditorFormType[]>([]);
/** Stores the ID of the last activated form. */
let lastActivatedId = $state<WorkspaceEditorFormType | undefined>();
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
	get lastActivatedId(): WorkspaceEditorFormType | undefined {
		return lastActivatedId;
	},
	get activeForms(): FormAttributeType[] {
		return activeForms;
	},
	get anyFormsActive(): boolean {
		return anyFormsActive;
	},

	/** Setters. */
	set lastActivatedId(newVal: WorkspaceEditorFormType) {
		lastActivatedId = newVal;
	},

	/**
	 * Activates a form.
	 * @param id ID of the form to activate.
	 * @param options Used to configure initial data for forms.
	 */
	activateForm(id: WorkspaceEditorFormType, options?: Record<string, any>) {
		if (!activeFormIds.includes(id)) {
			activeFormIds.push(id);
		}
		lastActivatedId = id;
	},
	/**
	 * Deactivate a form.
	 * @param id ID of the form to deactivate
	 */
	deactivateForm(id: WorkspaceEditorFormType) {
		if (activeFormIds.includes(id)) {
			activeFormIds = activeFormIds.filter((item) => item !== id);
		}
		if (!anyFormsActive) {
			lastActivatedId = undefined;
		}
	}
};
export default forms;
