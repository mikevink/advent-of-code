def max_heap(array: list[int], chroot: int, lena: int):
    maximum: int = chroot
    left: int = 2 * chroot + 1
    right: int = 2 * chroot + 2

    if left < lena and array[maximum] <= array[left]:
        maximum = left

    if right < lena and array[maximum] <= array[right]:
        maximum = right

    if chroot != maximum:
        array[chroot], array[maximum] = array[maximum], array[chroot]

        max_heap(array, maximum, lena)


def heapsort(array: list[int]):
    lena: int = len(array)
    # build heap
    for i in range(lena // 2, -1, -1):
        max_heap(array, i, lena)
    # sort
    # we always work with 0, so no need to include it in the loop
    for i in range(lena - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        # last element of the array should already be max, so skip it
        lena -= 1
        max_heap(array, 0, lena)
