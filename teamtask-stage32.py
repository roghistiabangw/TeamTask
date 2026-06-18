# === Stage 32: Add pagination helpers for long console output ===
# Project: TeamTask
def paginate_output(lines, page_size=15):
    """Yields chunks of output lines for readable console paging."""
    total_pages = (len(lines) + page_size - 1) // page_size if lines else 0
    current_page = 0
    while True:
        start = current_page * page_size
        end = min(start + page_size, len(lines))
        yield lines[start:end]
        if not lines or end >= len(lines):
            break
        current_page += 1

def print_paged_output(data, title="Output", page_size=15):
    """Prints data in pages with navigation controls."""
    if not data:
        print(f"{title}: No data to display.")
        return
    total = len(data)
    print(f"\n{title} ({total} items)")
    print("-" * 40)
    page_num = 1
    while True:
        chunk = list(paginate_output(data, page_size))[page_num - 1] if page_num <= (len(data) + page_size - 1) // page_size else []
        for item in chunk:
            print(item)
        current_total = len(chunk)
        total_pages = (total + page_size - 1) // page_size
        print("-" * 40)
        if current_total < page_size or page_num >= total_pages:
            break
        next_input = input(f"[{page_num}/{total_pages}] Press 'n' for next, 'p' for previous, 'q' to quit: ").strip().lower()
        if next_input == "q":
            return
        elif next_input == "n":
            page_num += 1
        elif next_input == "p" and page_num > 1:
            page_num -= 1
