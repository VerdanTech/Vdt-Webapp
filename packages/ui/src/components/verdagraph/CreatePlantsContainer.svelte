<script lang="ts">
	import type { Vector2d } from 'konva/lib/types';

	import type { Geometry, GeometryUpdateCommand } from '@vdg-webapp/models';

	import { Plant } from '$components';

	import CreatePlantContainer from './CreatePlantContainer.svelte';
	import { getVerdagraphContext } from './verdagraphContext.svelte';

	type Props = {
		plantLayerId: string;
		workspaceId: string;
	};
	let { plantLayerId, workspaceId }: Props = $props();

	/** Contexts.*/
	const verdagraphContext = getVerdagraphContext();
	const canvas = verdagraphContext.layoutCanvasContext;
	const { form: formData } = verdagraphContext.plantsCreateForm.form;
</script>

<!--
@component
Renders plant(s) in the canvas representing the
plants creation form.

Should only render this component if the plants
creation tool is active.
-->
{#if $formData.mode === 'SINGLE'}
	<CreatePlantContainer {workspaceId} {plantLayerId} plantIdx={0} />
{:else if $formData.mode === 'GROUP'}{:else if $formData.mode === 'PATTERN'}{:else if $formData.mode === 'COMBINED'}{/if}
