<script lang="ts">
	import { getContext } from 'svelte';

	import { CONTROLLER_CONTEXT_ID, type ControllerContext } from '@vdg-webapp/models';
	import { Verdagraph, setGardenContext, setVerdagraphContext } from '@vdg-webapp/ui';

	import { gardenId } from './seed';

	const controller = getContext<ControllerContext>(CONTROLLER_CONTEXT_ID);
	const verdagraph = setVerdagraphContext();
	const garden = setGardenContext(controller);
	garden.id = gardenId;
</script>

<Verdagraph gardenId={garden.id} />
