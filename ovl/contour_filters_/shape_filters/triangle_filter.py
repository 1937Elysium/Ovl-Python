import cv2

from ovl import contour_filter, triangle_fill_ratio


@contour_filter
def triangle_filter(contour_list, min_area_ratio=0.8, approximation_coefficient=0.02):
    """
    Receives a list of contours and returns only those that are approximately
    triangle and have 3
    :param approximation_coefficient: the approximation coefficient affects
    how the contour's perimeter is approximated, the larger the number is (out of 1) the more the approximation of
    the contour is a line
    :param contour_list: the list of contours to be filtered
    :param min_area_ratio: the minimum ratio between the area of the contour and the bounding triangle
    :return: the filtered list
    """
    output_list = []
    ratio_list = []
    if type(contour_list) is not list:
        contour_list = [contour_list]
    for current_contour in contour_list:
        fill_ratio = triangle_fill_ratio(current_contour)
        peri = cv2.arcLength(current_contour, True)
        approximation = cv2.approxPolyDP(current_contour, approximation_coefficient * peri, True)
        if fill_ratio > min_area_ratio and len(approximation) == 3:
            ratio_list.append(fill_ratio)
            output_list.append(current_contour)
    return output_list, ratio_list