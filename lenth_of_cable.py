from rich import print
import heapq

def min_cost(cable_lengths):
    if not cable_lengths:
        return 0

    heapq.heapify(cable_lengths)
    total_cost = 0
    step = 1

    print("[bold cyan]Початкова купа:[/bold cyan]", cable_lengths)

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        union = first + second
        prev_total_cost = total_cost
        total_cost += union
        heapq.heappush(cable_lengths, union)

        print(f"\n[bold yellow]Крок {step}[/bold yellow]:")
        print(f"  [green]Вибрано:[/green] {first} і {second}")
        print(f"  [magenta]Сума:[/magenta] {union}")
        print(f"  [blue]Купа після додавання:[/blue] {cable_lengths}")
        print(f"  [red]Поточна вартість:[/red] {prev_total_cost} + {union} = {total_cost}")
        step += 1

    print(f"\n[bold green]Загальні витрати:[/bold green] {total_cost}")
    return total_cost

# Приклад виклику
cables = [1, 3, 5, 9]
min_cost(cables)
