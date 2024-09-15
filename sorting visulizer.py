import pygame
import random

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithm Visualizer")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


array = []
array_size = 50
sorting = False
algorithm = None

def generate_array(size):
    return [random.randint(10, 100) for _ in range(size)]

def draw_array(array, color_position=None):
    window.fill(WHITE)
    bar_width = width // len(array)
    for i, val in enumerate(array):
        color = RED if color_position and i in color_position else BLUE
        pygame.draw.rect(window, color, (i * bar_width, height - val * 5, bar_width - 2, val * 5))
    pygame.display.update()


# Bubble Sort Algorithm
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            draw_array(array, [j, j+1])
            pygame.time.delay(30)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            draw_array(array)
    return array


# Merge Sort Algorithm
def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def merge(array, left, mid, right):
    left_part = array[left:mid+1]
    right_part = array[mid+1:right+1]
    
    i = j = 0
    k = left
    
    while i < len(left_part) and j < len(right_part):
        draw_array(array, [k])
        pygame.time.delay(30)
        if left_part[i] < right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1
        draw_array(array)
    
    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1
        draw_array(array)
        pygame.time.delay(30)
    
    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1
        draw_array(array)
        pygame.time.delay(30)


# Quick Sort Algorithm
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        draw_array(array, [i, j, high])
        pygame.time.delay(30)
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            draw_array(array)
    
    array[i+1], array[high] = array[high], array[i+1]
    draw_array(array, [i+1])
    return i+1


# Insertion Sort Algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            draw_array(array, [j, j+1])
            pygame.time.delay(30)
            j -= 1
        array[j + 1] = key
        draw_array(array)


# Selection Sort Algorithm
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            draw_array(array, [i, j])
            pygame.time.delay(30)
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(array, [i, min_idx])


# Heap Sort Algorithm
def heap_sort(array):
    n = len(array)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        draw_array(array, [i, 0])
        pygame.time.delay(30)
        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        draw_array(array, [i, largest])
        pygame.time.delay(30)
        heapify(array, n, largest)


# Function to reset and randomize the array
def reset_array():
    global array
    array = generate_array(array_size)
    draw_array(array)


# Main loop
running = True
reset_array()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keydown event to start the sorting algorithm
        if event.type == pygame.KEYDOWN:
            # Reset the array when 'R' is pressed
            if event.key == pygame.K_r:
                reset_array()

            # Select and run the Bubble Sort algorithm when 'B' is pressed
            if event.key == pygame.K_b and not sorting:
                sorting = True
                bubble_sort(array)
                sorting = False

            # Select and run the Merge Sort algorithm when 'M' is pressed
            if event.key == pygame.K_m and not sorting:
                sorting = True
                merge_sort(array, 0, len(array) - 1)
                sorting = False

            # Select and run the Quick Sort algorithm when 'Q' is pressed
            if event.key == pygame.K_q and not sorting:
                sorting = True
                quick_sort(array, 0, len(array) - 1)
                sorting = False

            # Select and run the Insertion Sort algorithm when 'I' is pressed
            if event.key == pygame.K_i and not sorting:
                sorting = True
                insertion_sort(array)
                sorting = False

            # Select and run the Selection Sort algorithm when 'S' is pressed
            if event.key == pygame.K_s and not sorting:
                sorting = True
                selection_sort(array)
                sorting = False

            # Select and run the Heap Sort algorithm when 'H' is pressed
            if event.key == pygame.K_h and not sorting:
                sorting = True
                heap_sort(array)
                sorting = False

    # Draw the unsorted array
    if not sorting:
        draw_array(array)

pygame.quit()
