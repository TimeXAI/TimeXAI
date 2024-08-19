"""Implementation of a Gaussian mixture sampler.

Available models:
------------------

.. autosummary::
    ~XGen.models.AE
    ~XGen.models.VAE
    ~XGen.models.BetaVAE
    ~XGen.models.VAE_LinNF
    ~XGen.models.VAE_IAF
    ~XGen.models.DisentangledBetaVAE
    ~XGen.models.FactorVAE
    ~XGen.models.BetaTCVAE
    ~XGen.models.IWAE
    ~XGen.models.MSSSIM_VAE
    ~XGen.models.WAE_MMD
    ~XGen.models.INFOVAE_MMD
    ~XGen.models.VAMP
    ~XGen.models.SVAE
    ~XGen.models.Adversarial_AE
    ~XGen.models.VAEGAN
    ~XGen.models.VQVAE
    ~XGen.models.HVAE
    ~XGen.models.RAE_GP
    ~XGen.models.RAE_L2
    ~XGen.models.RHVAE
    :nosignatures:
"""

from .gaussian_mixture_config import GaussianMixtureSamplerConfig
from .gaussian_mixture_sampler import GaussianMixtureSampler

__all__ = ["GaussianMixtureSampler", "GaussianMixtureSamplerConfig"]
