<script lang="ts">
	import { goto } from '$app/navigation'
	import Icon from '@iconify/svelte'
	import * as Form from '$lib/components/ui/form'
	import { Button } from '$lib/components/ui/button'
	import { Input } from '$lib/components/ui/input'
	import { Textarea } from '$lib/components/ui/textarea'
	import { superForm, defaults } from 'sveltekit-superforms'
	import { zod } from 'sveltekit-superforms/adapters'
	import { gardenCreate } from '$lib/data/garden/commands'
	import { createServerErrors } from '$state/formServerErrors.svelte'
	import iconIds from '$lib/assets/icons'
	import { gardenGenerateUniqueKeyQuery } from '$data/garden/queries'
	/* Form mutation. */
	const mutation = gardenCreate.mutation()
	/* Server error state. */
	const serverErrors = createServerErrors()

	/**
	 * Standard form configuration:
	 * - SPA: True disables server-side functionality.
	 * - validators: Zod schema specifies form validation.
	 * - onUpdate: Submission handler. Activates svelte-query mutation,
	 *  executes success task, and sets server errors on failure.
	 * - onChange: Reset server errors.
	 */
	const form = superForm(defaults(zod(gardenCreate.schema)), {
		SPA: true,
		validators: zod(gardenCreate.schema),
		onUpdate({ form }) {
			if (form.valid) {
				$mutation.mutate(form.data, {
					onSuccess: () => {
						/**
						 * TODO: Move this state update to the data layer.
						 * It is here because having both onSuccess callbacks
						 * caused only the first to be run.
						 */
						goto('/app/gardens/' + form.data.key)
					},
					onError: (error) => {
						// @ts-ignore
						serverErrors.setErrors(error)
					}
				})
			}
		},
		onChange() {
			serverErrors.reset()
		}
	})
	const { form: formData, enhance } = form
</script>

<form method="POST" use:enhance>
	<!-- Garden name -->
	<Form.Field {form} name="name">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.name.description}
				>Name</Form.Label
			>
			<Input
				{...attrs}
				type="text"
				placeholder="Gardens of Adonis"
				bind:value={$formData.name}
			/>
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['name']} />
	</Form.Field>

	<!-- Garden key -->
	<Form.Field {form} name="key">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.key.description}
				>Key</Form.Label
			>
			<span class="flex">
				<Input
					{...attrs}
					type="text"
					placeholder="lettuce123"
					class="rounded-r-none"
					bind:value={$formData.key}
				/>
				<Button
					variant="outline"
					class="flex items-center rounded-l-none border-l-0 border-neutral-12"
				>
					<Icon icon={iconIds.defaultRefreshIcon} width="1.5rem" />
				</Button>
			</span>
		</Form.Control>
		<Form.Description>Readable identifier, used in URLs.</Form.Description>
		<Form.FieldErrors serverErrors={serverErrors.errors['key']} />
	</Form.Field>

	<!-- Garden visibility -->
	<Form.Field {form} name="visibility">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.visibility.description}
				>Visibility</Form.Label
			>
			<Input {...attrs} placeholder="Private" bind:value={$formData.visibility} />
		</Form.Control>
		<Form.Description
			>Private gardens can only be viewed by members. Unlisted gardens can be viewed by
			anyone with a link. Public gardens are searchable.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['visibility']} />
	</Form.Field>

	<!-- Garden description -->
	<Form.Field {form} name="description">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.description.description}
				>Description</Form.Label
			>
			<Textarea {...attrs} bind:value={$formData.description} />
		</Form.Control>
		<Form.FieldErrors serverErrors={serverErrors.errors['description']} />
	</Form.Field>

	<!-- Admins to invite -->
	<Form.Field {form} name="admin_ids">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.admin_ids.description}
				>Admin Invites</Form.Label
			>
			<Input {...attrs} placeholder="" bind:value={$formData.admin_ids} />
		</Form.Control>
		<Form.Description>Admins have full control over the garden.</Form.Description>
		<Form.FieldErrors serverErrors={serverErrors.errors['admin_ids']} />
	</Form.Field>

	<!-- Editors to invite -->
	<Form.Field {form} name="editor_ids">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.editor_ids.description}
				>Editor Invites</Form.Label
			>
			<Input {...attrs} placeholder="" bind:value={$formData.editor_ids} />
		</Form.Control>
		<Form.Description
			>Editors have limited write access but cannot change garden configuration.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['editor_ids']} />
	</Form.Field>

	<!-- Viewers to invite -->
	<Form.Field {form} name="viewer_ids">
		<Form.Control let:attrs>
			<Form.Label description={gardenCreate.schema.shape.viewer_ids.description}
				>Viewer Invites</Form.Label
			>
			<Input {...attrs} placeholder="" bind:value={$formData.viewer_ids} />
		</Form.Control>
		<Form.Description
			>Viewers can make no changes but can view everything.</Form.Description
		>
		<Form.FieldErrors serverErrors={serverErrors.errors['viewer_ids']} />
	</Form.Field>

	<!-- Submit button -->
	<Form.Button
		disabled={false}
		loading={$mutation.isLoading}
		variant="default"
		class="mt-4 w-full">Create</Form.Button
	>
</form>
