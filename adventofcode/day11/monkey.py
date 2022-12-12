from queue import Queue
from typing import Callable


class Monkey:
    def __init__(
        self,
        id: int,
        items: Queue,
        operation: Callable[[int], int],
        condition: Callable[[int], bool],
        true_op: int,
        false_op: int,
        divisor: int,
    ):
        self.id: int = id
        self.items: Queue = items
        self.operation: Callable[[int], int] = operation
        self.condition: Callable[[int], bool] = condition
        self.true_op: int = true_op
        self.false_op: int = false_op
        self.inspection_count = 0
        self.divisor: int = divisor

    def operate(self, item: int) -> int:
        self.inspection_count += 1
        return self.operation(item)

    def eval(self, item: int) -> int:
        if self.condition(item) == 0:
            return self.true_op
        else:
            return self.false_op

    def build_operator(raw: str) -> Callable[[int], int]:
        op = raw.removeprefix("  Operation: new = ")
        parts = op.split(" ")
        op = parts[1]
        if parts[2] == "old":
            self_mutate = True
        else:
            self_mutate = False
            operand = int(parts[2])
        match op:
            case "+":
                if self_mutate:
                    return lambda x: x + x
                else:
                    return lambda x: x + operand
            case "*":
                if self_mutate:
                    return lambda x: x * x
                    # return lambda x: x
                else:
                    return lambda x: x * operand


def build_monkey(input: list[str]) -> Monkey:
    id = int(input[0].split(" ")[1].removesuffix(":"))
    items_list = [int(x.strip()) for x in input[1].split(":")[1].split(",")]
    items = Queue()
    [items.put(i) for i in items_list]
    operation = Monkey.build_operator(input[2])
    divisor = int(input[3].split(" ")[-1])
    evaluation = lambda x: (x % divisor)
    true_op = int(input[4].split(" ")[-1])
    false_op = int(input[5].split(" ")[-1])
    return Monkey(id, items, operation, evaluation, true_op, false_op, divisor)
