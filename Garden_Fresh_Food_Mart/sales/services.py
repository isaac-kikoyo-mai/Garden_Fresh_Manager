from decimal import Decimal


def process_sale(product, quantity_sold):

    remaining_qty = quantity_sold

    total_cost = Decimal("0.00")

    batches = InventoryBatch.objects.filter(
        product=product,
        quantity_remaining__gt=0
    ).order_by('purchase_date')

    available_stock = sum(
        batch.quantity_remaining
        for batch in batches
    )

    if available_stock < quantity_sold:
        raise ValueError(
            f"Only {available_stock} items available."
        )

    for batch in batches:

        if remaining_qty <= 0:
            break

        qty_from_batch = min(
            remaining_qty,
            batch.quantity_remaining
        )

        unit_cost = (
            batch.total_cost /
            batch.quantity_received
        )

        total_cost += (
            qty_from_batch * unit_cost
        )

        batch.quantity_remaining -= qty_from_batch
        batch.save()

        remaining_qty -= qty_from_batch

    return total_cost