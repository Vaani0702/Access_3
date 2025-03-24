from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Course, UserCertificate

# Change to accept both GET and POST for compatibility
@api_view(['GET', 'POST'])
def recommend_courses(request):
    # Handle both GET and POST methods
    if request.method == 'GET':
        user_disability = request.GET.get('disability', '')
    else:  # POST
        user_disability = request.data.get('disability', '')
    
    if not user_disability:
        return Response({"error": "Disability type required"}, status=400)

    # Filter courses based on the disability category
    courses = Course.objects.filter(category__icontains=user_disability)
    
    # If no courses found with exact category match, try to find any related courses
    if not courses.exists():
        # Try to find in title or description
        courses = Course.objects.filter(
            Q(title__icontains=user_disability) | 
            Q(description__icontains=user_disability)
        )
    
    # Convert to list of dictionaries for JSON response
    courses_data = [{
        'title': course.title,
        'description': course.description,
        'image_url': course.image_url,
        'external_url': course.external_url,
    } for course in courses]
    
    return Response({"courses": courses_data})

@api_view(['POST'])
def upload_certificate(request):
    user_name = request.data.get('user_name')
    certificate_file = request.FILES.get('certificate')
    
    if not user_name or not certificate_file:
        return Response({'message': 'Both user_name and certificate are required'}, status=400)
    
    try:
        # Save the certificate to the database
        certificate = UserCertificate.objects.create(
            user_name=user_name,
            certificate=certificate_file
        )
        return Response({'message': 'Certificate uploaded successfully! You will receive your NFT soon.'})
    except Exception as e:
        return Response({'message': f'Error uploading certificate: {str(e)}'}, status=500)