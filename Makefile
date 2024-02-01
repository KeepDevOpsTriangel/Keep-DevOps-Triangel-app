# Variables used to configure docker images
IMAGE_REGISTRY_DOCKERHUB 	?= kctriangle
IMAGE_REGISTRY_GHCR			?= ghcr.io
IMAGE_REPO					= keepdevopstriangel
IMAGE_NAME					?= triangle-bot
VERSION						?= develop

# Variables used to configure docker images registries to build and push
IMAGE 				= $(IMAGE_REGISTRY_DOCKERHUB)/$(IMAGE_NAME):$(VERSION)
IMAGE_LATEST 		= $(IMAGE_REGISTRY_DOCKERHUB)/$(IMAGE_NAME):latest
IMAGE_GHCR			= $(IMAGE_REGISTRY_GHCR)/$(IMAGE_REPO)/$(IMAGE_NAME):$(VERSION)
IMAGE_GHRC_LATEST	= $(IMAGE_REGISTRY_GHCR)/$(IMAGE_REPO)/$(IMAGE_NAME):latest

.PHONY: docker-build
docker-build: ## Build image
	docker buildx build --push --platform=linux/amd64,linux/arm64 . -t
$(IMAGE) -t $(IMAGE_LATEST) -t $(IMAGE_GHCR) -t $(IMAGE_GHRC_LATEST)

.PHONY: publish
publish: docker-build ## Publish image
	docker push $(IMAGE)
	docker push $(IMAGE_LATEST)
	docker push $(IMAGE_GHCR)
	docker push $(IMAGE_GHRC_LATEST)