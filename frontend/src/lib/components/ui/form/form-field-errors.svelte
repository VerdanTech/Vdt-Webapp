<script lang="ts">
	import * as FormPrimitive from 'formsnap';
	import { cn } from '$lib/utils/shadcn.js';

	type $$Props = FormPrimitive.FieldErrorsProps & {
		errorClasses?: string | undefined | null;
		serverErrors?: string[] | undefined | null;
	};

	let className: $$Props['class'] = undefined;
	export { className as class };
	export let errorClasses: $$Props['class'] = undefined;
	export let serverErrors: $$Props['serverErrors'] = [];
</script>

<FormPrimitive.FieldErrors
	class={cn('text-sm font-medium text-warning-11', className)}
	{...$$restProps}
	let:errors
	let:fieldErrorsAttrs
	let:errorAttrs
>
	<slot {errors} {fieldErrorsAttrs} {errorAttrs}>
		<ul>
			{#each errors as error}
				<li
					{...errorAttrs}
					class={cn(
						errorClasses,
						'border-x border-warning-7 bg-warning-3 p-1 first:rounded-t-md first:border-t last:mb-4 last:rounded-b-md last:border-b'
					)}
				>
					{error}
				</li>
			{/each}
			{#if serverErrors}
				{#each serverErrors as error}
					<li
						{...errorAttrs}
						class={cn(
							errorClasses,
							'border-x border-warning-7 bg-warning-3 p-1 first:rounded-t-md first:border-t last:mb-4 last:rounded-b-md last:border-b'
						)}
					>
						{error}
					</li>
				{/each}
			{/if}
		</ul>
	</slot>
</FormPrimitive.FieldErrors>
